import React from 'react';
import TestLauncher from './TestLauncher.js';
import ProcessingLauncher from './ProcessingLauncher.js';
import VisualLauncher from './VisualLauncher.js';

function LauncherParent() {
  return (
      <div class="column">
          <TestLauncher/>
          <ProcessingLauncher/>
          <VisualLauncher/>
      </div>
  );
}

export default LauncherParent;
