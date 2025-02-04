import { ReactNode, useContext } from "react"
import { FrameBox } from "../atoms/atoms"
import StateContext, { AppState } from "../contexts/state"
import ConfigPage from "./configPage"
import TaskPage from "./taskPage"

const BodyContents = () => {
  const { appState } = useContext(StateContext)

  const StateItem: Record<AppState, ReactNode> = {
    "-1": <>No Items</>,
    "TASK"  : <TaskPage/>,
    "CONFIG": <ConfigPage/>
  }

  return (<FrameBox width="100%" align="center" justify="center" bgColor="#00F5">
    {StateItem[appState.state]}
  </FrameBox>)
}

export default BodyContents

