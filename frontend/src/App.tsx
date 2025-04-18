import unitLogo from './assets/unit.png'
import unitBg from './assets/bg.png'

function App() {
  return (
    <div
      className="w-screen h-screen bg-cover bg-center flex flex-col items-center justify-center text-white text-center"
      style={{ backgroundImage: `url(${unitBg})` }}
    >
      <a
        href="https://discord.gg/taskforce121"
        target="_blank"
        rel="noopener noreferrer"
        className="flex justify-center"
      >
        <img src={unitLogo} alt="Task Force Logo" className="w-144 max-w-[50%] mb-6" />
      </a>
      <h1 className="text-4xl font-bold">Task Force 121</h1>
      <h2 className="text-2xl mt-2">Under Construction</h2>
    </div>
  )
}

export default App
