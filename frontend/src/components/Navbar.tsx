function NavBar(){
    const token = localStorage.getItem("token")

    return(
        <nav>   
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/cart">Cart</a>
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