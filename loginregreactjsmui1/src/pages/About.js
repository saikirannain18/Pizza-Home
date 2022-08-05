import React from "react";
// import Groco from "../assets/grocery.jpg";
import MultiplePizzas from "../assets/multiplePizzas.jpeg";
import "../styles/About.css";
function About() {
  return (
    <div className="about">
      
      <div
        className="aboutTop"
        style={{ backgroundImage: `url(${MultiplePizzas})` }}
      ></div>
      <div className="aboutBottom">
        <h1> ABOUT US</h1>

        <p>
        Pizza-Home has a rich history of developing innovations that have made a significant impact on the pizza and delivery industries. Is Pizza-Home a pizza company with great technology, or are we a technology company that just happens to sell pizza? We’ll let you be the judge!
        </p>
        
        
      </div>
    </div>
  );
}

export default About;