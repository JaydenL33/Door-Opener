import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';



class Navbar extends Component {
    render () {
        return (
        <header id ="nav">
            <ul className="nav_links">
                <li>
                    <Link to="/">Login Menu</Link>
                </li>
            </ul>
        </header>
        );
    }
}

export default Navbar;