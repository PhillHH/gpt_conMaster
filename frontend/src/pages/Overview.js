import React from 'react';

import ContentBox from '../components/ContentBox';
import InfoCard from '../components/InfoCard';
import ChatList from '../components/chatList';

function Overview() {
  return (
    <ContentBox>
      <div className="boxcontent">
        <h1>Overview</h1>
        <ChatList />

        <div className="info-cards-container">
          <InfoCard
            title="ChatGPT Conversation Manager"
            text="Efficiently manage and organize your ChatGPT conversations. With our user-friendly tool, you can easily track, filter, search, and save your chats as needed."
            image="path/to/your/expert-image.jpg"
            linkText="Coming soon"
            linkHref="#"
          />
          <InfoCard
            title=" Prompt Engineering Tool"
            text="Develop precise and effective prompts for your AI-driven applications. Our tool provides all the necessary features to craft tailored inputs and achieve the desired outcomes."
            image="path/to/your/approval-image.jpg"
            linkText="Coming soon"
            linkHref="#"
          />
         
        </div>

        <div class="announcement">
        <h2 class="announcement-title">🚀 Exciting Developments Ahead with GPT_ConMaster! 🚀</h2>
        <p class="announcement-text">
            We are thrilled to share the progress we’re making with GPT_ConMaster – a cutting-edge platform designed to revolutionize the way you manage and interact with AI-driven conversations.
        </p>
        <p class="announcement-text">
            Every single day, we are hard at work, pushing boundaries and bringing new features to life. Our dedication to innovation drives us to continuously enhance and expand the capabilities of GPT_ConMaster. Whether it’s refining the user experience, adding powerful new tools, or improving performance, we are committed to making this platform the best it can be.
        </p>
        <p class="announcement-text">
            But we’re not stopping there – our vision for GPT_ConMaster is big, and we’re just getting started. We invite you to follow our journey as we build something truly transformative. Stay tuned for exciting updates and new features that will take your AI interaction to the next level!
        </p>
        <p class="announcement-text">
            Join us on this incredible journey, and be part of the future of AI-driven communication.
        </p>

        <h2 class="announcement-title">🚀 Exciting Developments Ahead with GPT_ConMaster! 🚀</h2>
        <p class="announcement-text">
            We are thrilled to share the progress we’re making with GPT_ConMaster – a cutting-edge platform designed to revolutionize the way you manage and interact with AI-driven conversations.
        </p>
        <p class="announcement-text">
            Every single day, we are hard at work, pushing boundaries and bringing new features to life. Our dedication to innovation drives us to continuously enhance and expand the capabilities of GPT_ConMaster. Whether it’s refining the user experience, adding powerful new tools, or improving performance, we are committed to making this platform the best it can be.
        </p>
        <p class="announcement-text">
            But we’re not stopping there – our vision for GPT_ConMaster is big, and we’re just getting started. We invite you to follow our journey as we build something truly transformative. Stay tuned for exciting updates and new features that will take your AI interaction to the next level!
        </p>
        <p class="announcement-text">
            Join us on this incredible journey, and be part of the future of AI-driven communication.
        </p>


       

    </div>


        {/* letzten Aktivitäte  */}
      </div>
    </ContentBox>
  );
}

export default Overview;