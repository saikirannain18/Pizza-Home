


import React from 'react'
import {Link} from "react-router-dom";
import BannerImage from "../assets/pizza2.jpg";
import "../styles/Home.css";

function Home() {
  return (
    <div className='home' style={{backgroundImage:`url(${BannerImage})`}}>
      <div className='headerContainer' >
          <h1>Pizza-Home</h1>
          <p>Never sit around and wait for someone <br/>Unless they’re delivering a pizza </p>
        <Link to="/menu">
          
          <button >OrderNow</button>
        </Link>

      </div>
    </div>
  )
}

export default Home

