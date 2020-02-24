import React from 'react';
import ParametersParent from './Parameters/ParametersParent.js';
import LauncherParent from './Launchers/LauncherParent';
import './App.css';

function App() {
  return (
    <div className="App">
      <div class="columns">
        <ParametersParent/>
        <LauncherParent/>
      </div>
    </div>
  );
}

export default App;
