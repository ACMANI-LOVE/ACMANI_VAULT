import { StateType } from "@/const/type"
import { createContext } from "react"

export type AppState = "-1"|"TASK"|"CONFIG"
export type GroupState = "-1"|"SELECT"|"EDIT"|"CONFIRM"
export type BodyState = "-1"|"IDLE"|"REQUEST"|"PROMPT"|"POSTING"

export type StateContextType = {
  sideMenuState: StateType<boolean>
  appState: StateType<AppState>
  groupState:StateType<GroupState>
  bodyState:StateType<BodyState>
}


const StateContext = createContext<StateContextType>({
  sideMenuState: {
    state: false,
    setState: () => { }
  },
  appState: {
    state: "-1",
    setState: () => { }
  },
  groupState: {
    state: "-1",
    setState: () => { }
  },
  bodyState: {
    state: "-1",
    setState: () => { }
  },
})

export default StateContext

