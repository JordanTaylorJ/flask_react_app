import Login from "./login/page"
import Navbar from "./components/Navbar"
import Logs from "./logs/page"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12">
      <Navbar/>
      <p>Welcome</p>
      <Login/>
      <Logs/>
    </main>
  )
}
