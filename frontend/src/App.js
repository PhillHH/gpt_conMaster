import React, { useState } from 'react';
import Sidebar_UI from './components/Sidebar_UI'; // Importiere die Sidebar-Komponente
import ContentBox from './components/ContentBox'; // Importiere die ContentBox-Komponente
import './App.css'; // Importiere die globale CSS-Datei

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
