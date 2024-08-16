import React, { useState } from 'react';
import Sidebar_UI from './components/Sidebar_UI';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ContentBox from './components/ContentBox';
import Overview from './pages/Overview';
import FloatingStaff from './components/FloatingStaff';
import FloatingStaff_02 from './components/FloatingStaff_02';
import './App.css';

function App() {
    const [isCollapsed, setIsCollapsed] = useState(false);

    const toggleSidebar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
        <Router>
            <div className={`App ${isCollapsed ? 'collapsed' : ''}`}>
                <Sidebar_UI isCollapsed={isCollapsed} toggleSidebar={toggleSidebar} />
                <Routes>
                    <Route path="/overview" element={<Overview />} />
                    {/* Weitere Routen können hier hinzugefügt werden */}
                </Routes>
                {/* Hier wird die ContentBox für die Startseite hinzugefügt */}
                <Routes>
             
                    <Route path="/" element={
                        <ContentBox>
                            <h1>Home</h1>
                            <h2>The Current Team: 
                                
                                Lets do something big! </h2>
                            <div className='.floating-staff-container'>
                      <FloatingStaff />
                      
                             </div>
                        </ContentBox>
                    } />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
