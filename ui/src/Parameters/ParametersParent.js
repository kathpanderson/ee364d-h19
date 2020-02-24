import React from 'react';
import HardwareParameters from './HardwareParameters.js';
import ProcessingParameters from './ProcessingParameters.js';

function ParametersParent() {
  return (
      <div class="column is-bordered-right is-two-fifths">
          <HardwareParameters/>
          <ProcessingParameters/>
      </div>
  );
}

export default ParametersParent;
