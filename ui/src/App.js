import React from 'react';
import ParametersPanel from './ParametersPanel.js';
import LauncherPanel from './LauncherPanel';
import './App.css';

function App() {
  return (
    <div className="App">
      <div class="columns">
        <ParametersPanel/>
        <LauncherPanel/>
      </div>
    </div>
  );
}

export default App;
