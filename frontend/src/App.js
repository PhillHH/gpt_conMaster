import React, { useState } from 'react';
import Sidebar_UI from './components/Sidebar_UI';
import ContentBox from './components/ContentBox';
import './App.css';

function App() {
    const [isCollapsed, setIsCollapsed] = useState(false);

    const toggleSidebar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
        <div className={`App ${isCollapsed ? 'collapsed' : ''}`}>
            <Sidebar_UI isCollapsed={isCollapsed} toggleSidebar={toggleSidebar} />
            <ContentBox>
                <h1>Overview</h1>
                <p>This will be a huge project soon. Make things happen with Growento.com:</p>
            </ContentBox>
        </div>
    );
}

export default App;