import React from 'react';
import HardwareParameters from './Parameters/HardwareParameters.js';
import ProcessingParameters from './Parameters/ProcessingParameters.js';

function ParametersPanel() {
  return (
      <div class="column is-bordered-right">
          <HardwareParameters/>
          <ProcessingParameters/>
      </div>
  );
}

export default ParametersPanel;
