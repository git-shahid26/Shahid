import React, { useState } from 'react';
import { ArrowRight, CheckCircle, ChevronRight, UserCircle, FileText, Settings, BarChart2 } from 'lucide-react';

const WorkflowApp = () => {
  const [activeModule, setActiveModule] = useState('bol');
  const [completedSteps, setCompletedSteps] = useState([]);

  const modules = {
    bol: {
      title: 'BOL Processing',
      icon: FileText,
      steps: ['Document Upload', 'Payment Processing', 'Receipt Generation'],
      nextModule: 'bob'
    },
    bob: {
      title: 'BOB Processing',
      icon: Settings,
      steps: ['Contract Verification', 'Credit Check', 'Payment Terms'],
      nextModule: 'admin'
    },
    admin: {
      title: 'Administrative',
      icon: UserCircle,
      steps: ['Access Management', 'User Controls', 'Department Setup'],
      nextModule: 'ops'
    },
    ops: {
      title: 'Operations',
      icon: BarChart2,
      steps: ['Sales Entry', 'Tax Classification', 'Analytics'],
      nextModule: null
    }
  };

  const handleStepComplete = (step) => {
    if (!completedSteps.includes(step)) {
      setCompletedSteps([...completedSteps, step]);
    }
  };

  const handleNextModule = () => {
    const next = modules[activeModule].nextModule;
    if (next) {
      setActiveModule(next);
    }
  };

  const ModuleIcon = modules[activeModule].icon;

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-md p-4">
        <div className="max-w-6xl mx-auto flex justify-between items-center">
          <h1 className="text-xl font-bold">System Workflow</h1>
          <div className="flex space-x-4">
            {Object.entries(modules).map(([key, module]) => {
              const Icon = module.icon;
              return (
                <button
                  key={key}
                  onClick={() => setActiveModule(key)}
                  className={`flex items-center px-4 py-2 rounded-lg ${
                    activeModule === key ? 'bg-blue-100 text-blue-700' : 'text-gray-600'
                  }`}
                >
                  <Icon className="w-4 h-4 mr-2" />
                  {module.title}
                </button>
              );
            })}
          </div>
        </div>
      </nav>

      <main className="max-w-4xl mx-auto mt-8 p-6">
        <div className="bg-white rounded-xl shadow-lg p-6">
          <div className="flex items-center mb-6">
            <ModuleIcon className="w-8 h-8 text-blue-600 mr-3" />
            <h2 className="text-2xl font-bold">{modules[activeModule].title}</h2>
          </div>

          <div className="space-y-4">
            {modules[activeModule].steps.map((step, index) => (
              <div
                key={index}
                className="flex items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100 cursor-pointer"
                onClick={() => handleStepComplete(step)}
              >
                {completedSteps.includes(step) ? (
                  <CheckCircle className="w-6 h-6 text-green-500 mr-4" />
                ) : (
                  <div className="w-6 h-6 rounded-full border-2 border-gray-300 mr-4" />
                )}
                <span className="flex-1">{step}</span>
                <ChevronRight className="w-5 h-5 text-gray-400" />
              </div>
            ))}
          </div>

          {modules[activeModule].nextModule && (
            <button
              onClick={handleNextModule}
              className="mt-6 w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 flex items-center justify-center"
            >
              Next Module
              <ArrowRight className="ml-2 w-5 h-5" />
            </button>
          )}
        </div>

        <div className="mt-6 bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-lg font-semibold mb-4">Progress Overview</h3>
          <div className="flex justify-between items-center">
            <div className="flex-1">
              <div className="h-2 bg-gray-200 rounded-full">
                <div
                  className="h-2 bg-green-500 rounded-full transition-all duration-300"
                  style={{
                    width: `${(completedSteps.length / (Object.values(modules).reduce((acc, curr) => acc + curr.steps.length, 0))) * 100}%`
                  }}
                />
              </div>
            </div>
            <span className="ml-4 text-sm text-gray-600">
              {completedSteps.length} / {Object.values(modules).reduce((acc, curr) => acc + curr.steps.length, 0)} steps completed
            </span>
          </div>
        </div>
      </main>
    </div>
  );
};

export default WorkflowApp;
