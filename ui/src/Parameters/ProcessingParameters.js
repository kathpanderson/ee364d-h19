import React from 'react';

const defaultSNRVal = 10;
const defaultPixelVal = 128;
const defaultDAQSamplingVal = 2;
const defaultDAQSamplingUnit = "kHz";

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

function generateTextParam(name, defaultVal, unit) {
  return (
    <div class="tile is-parent is-custom-tile">
      <div class="tile is-child option-label">{name}:</div>
      <div class="tile is-2 field is-marginless">
        <div class="control">
          <textarea class="textarea has-fixed-size" rows="1" placeholder={defaultVal}></textarea>
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
      {generateTextParam("Photodetector 1", defaultSNRVal, "dB")}
      {generateTextParam("Photodetector 2", defaultSNRVal, "dB")}
      {generateTextParam("Tip Current", defaultSNRVal, "dB")}
      {generateTextParam("Tip Bias", defaultSNRVal, "dB")}
    </div>
  );
}

function ImageParams() {
  return (
    <div class="tile is-vertical">
      <div class="tile subsection-title is-italic">Image Dimensions</div>
      {generateTextParam("x", defaultPixelVal, "pixels")}
      {generateTextParam("y", defaultPixelVal, "pixels")}
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
          <textarea class="textarea has-fixed-size" rows="1" placeholder={defaultDAQSamplingVal}></textarea>
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
    if (option === defaultDAQSamplingUnit) {
      options.push(<option value={option} selected>{option}</option>);
    }
    else {
      options.push(<option value={option}>{option}</option>);
    }
  });

  return options;
}

export default ProcessingParameters;
