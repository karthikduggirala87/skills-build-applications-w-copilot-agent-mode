import React from 'react';
import './App.css';

function App() {
  return (
    <div>
      <nav>
        <img src={require('./octofitapp-small.png')} alt="OctoFit Logo" className="logo" />
        <a href="/">Home</a>
        <a href="/activities">Activities</a>
        <a href="/teams">Teams</a>
        <a href="/leaderboard">Leaderboard</a>
        <a href="/workouts">Workouts</a>
      </nav>
      <header>
        <h1>OctoFit Tracker</h1>
        <p>Track your fitness, join teams, and compete!</p>
      </header>
      <main>
        <h2>Welcome to OctoFit Tracker</h2>
        <p>Get started by exploring the navigation menu above.</p>
        <button>Start Workout</button>
      </main>
    </div>
  );
}

export default App;
