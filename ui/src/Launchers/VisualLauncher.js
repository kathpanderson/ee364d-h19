import React from 'react';
import { SectionTitle, CustomButton } from '../lib.js';

class VisualLauncher extends React.Component {
  render() {
    return (
        <div class="tile is-vertical is-bordered-bottom is-parent">
          <SectionTitle title="Visualizer"/>
          <CustomButton name="Launch Visualizer"/>
        </div>
    );
  }

  launchButton() {
    return (
      <div class="tile is-parent is-custom-tile">
        <div class="tile is-child">
          <button>Launch Visualizer</button>
        </div>
      </div>
    )
  }
}


export default VisualLauncher;
