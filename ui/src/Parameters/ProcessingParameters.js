import React from 'react';

var defaultSNRVal = 10;

function ProcessingParameters() {
  return (
      <div class="tile is-vertical">
        <div class="tile has-text-weight-bold">Processing Parameters</div>
        {SNRParams()}
        {ImageParams()}
        {DAQParams()}
      </div>
  );
}

function generateTextParam(name, unit) {
  return (
    <div class="tile is-parent is-custom-tile">
      <div class="tile is-child option-label">{name}:</div>
      <div class="tile is-2 field is-marginless">
        <div class="control">
          <textarea class="textarea has-fixed-size" rows="1" placeholder={defaultSNRVal}></textarea>
        </div>
      </div>
      <div class="tile is-child option-unit">{unit}</div>
    </div>
  )
}

function SNRParams() {
  return (
    <div class="tile is-vertical">
      <div class="tile subsection-title is-italic">SNR</div>
      {generateTextParam("Photodetector 1", "dB")}
      {generateTextParam("Photodetector 2", "dB")}
      {generateTextParam("Tip Current", "dB")}
      {generateTextParam("Tip Bias", "dB")}
    </div>
  );
}

function ImageParams() {
  return (
    <div class="tile is-vertical">
      <div class="tile subsection-title is-italic">Image Dimensions</div>
      {generateTextParam("x", "pixels")}
      {generateTextParam("y", "pixels")}
    </div>
  );
}

function DAQParams() {
  return (
    <div class="tile is-vertical">
      <div class="tile subsection-title is-italic">DAQ Parameters</div>
      <div class="tile is-parent is-custom-tile">
      <div class="tile is-child option-label">Sampling Rate:</div>
      <div class="tile is-2 field is-marginless">
        <div class="control">
          <textarea class="textarea has-fixed-size" rows="1" placeholder={defaultSNRVal}></textarea>
        </div>
      </div>
      <div class="tile is-child option-unit">
        {DAQUnitDropDown()}
      </div>
    </div>
    </div>
  );
}

function DAQUnitDropDown() {
  return (
    <div class="field">
      <div class="control">
        <div class="select">
          <select>
            {generateDAQUnitOptions()}
          </select>
        </div>
      </div>
    </div>
  );
}

function generateDAQUnitOptions() {
  var optionsToProvide = [
    "Hz", "kHz", "MHz", "GHz" 
  ];

  var options = [];
  optionsToProvide.forEach(function(option) {
    options.push(<option value={option}>{option}</option>);
  });

  return options;
}

export default ProcessingParameters;
