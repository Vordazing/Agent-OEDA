import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MenuGrid from './menu';
import Tables from './addasic';
import Ipbd from './ipbd'


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MenuGrid />} />
        <Route path="/addasic" element={<Tables />} />
        <Route path="/ipbd" element={<Ipbd />} />
      </Routes>
    </Router>
  );
};

export default App;
