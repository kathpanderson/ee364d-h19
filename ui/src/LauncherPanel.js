import React from 'react';
import TestLauncher from './Launchers/TestLauncher.js';
import ProcessingLauncher from './Launchers/ProcessingLauncher.js';
import VisualLauncher from './Launchers/VisualLauncher.js';

function LauncherPanel() {
  return (
      <div class="column">
          <TestLauncher/>
          <ProcessingLauncher/>
          <VisualLauncher/>
      </div>
  );
}

export default LauncherPanel;
