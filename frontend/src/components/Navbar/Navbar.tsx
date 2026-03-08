import styles from './Navbar.module.css'

function NavBar(){
    const token = localStorage.getItem("token")

    return(
        <nav className={styles.nav}>   
            <div className={styles.links}>
                    <a href="/"><b>//</b>Home<b>/</b></a>
                    <a href="/about"><b>\\∩[</b>About<b>].//</b></a>
                    <a href="/products"><b>//</b>Products<b>/Σ</b></a>
                    <a href="/cart"><b>.(х)</b>Cart<b>∫∅</b></a>
                    <a href="https://t.me/Zixther"><b>{'<'}13</b>Contact<b>/{'>'}</b></a>
            </div>
            {token ?(
                <button onClick={() => {
                    localStorage.removeItem('token');
                    window.location.reload();
                }}>Logout</button>

            ): (
                <a href="/login" className={styles.loginLink}><b>∬</b>Login<b>λ</b></a>
            )}
        </nav>
    )

}

export default NavBar;