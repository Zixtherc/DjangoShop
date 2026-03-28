import { Link, useNavigate } from 'react-router-dom';
import styles from './Navbar.module.css';

function NavBar() {
    const token = localStorage.getItem("token");
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('token');
        navigate('/login'); 
    };

    return (
        <nav className={styles.nav}>   
            <div className={styles.links}>
                <Link to="/"><b>//</b>Home<b>/</b></Link>
                <Link to="/about"><b>\\∩[</b>About<b>].//</b></Link>
                <Link to="/products"><b>//</b>Products<b>/Σ</b></Link>
                <Link to="/cart"><b>.(х)</b>Cart<b>∫∅</b></Link>
                <a href="https://t.me/Zixther" target="_blank" rel="noreferrer">
                    <b>{'<'}13</b>Contact<b>/{'>'}</b>
                </a>
            </div>

            {token ? (
                <button onClick={handleLogout} className={styles.logoutBtn}>
                    Logout
                </button>
            ) : (
                <Link to="/login" className={styles.loginLink}>
                    <b>∬</b>Login<b>λ</b>
                </Link>
            )}
        </nav>
    );
}

export default NavBar;