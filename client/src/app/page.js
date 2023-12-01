import Login from "./components/Login"
import Navbar from "./components/Navbar"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12">
      <Navbar/>
      <p>Welcome</p>
      <Login/>
    </main>
  )
}
