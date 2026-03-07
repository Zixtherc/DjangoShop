import styles from './Navbar.module.css'

function NavBar(){
    const token = localStorage.getItem("token")

    return(
        <nav className={styles.nav}>   
            <div className={styles.links}>
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/cart">Cart</a>
            </div>
            {token ?(
                <button onClick={() => {
                    localStorage.removeItem('token');
                    window.location.reload();
                }}>Logout</button>

            ): (
                <a href="/login">Login</a>
            )}
        </nav>
    )

}

export default NavBar;