import { ThemeProvider } from "@emotion/react"
import { CssBaseline } from "@mui/material"
import { ReactNode, useState } from "react"
import { DataContext, DataContextType } from "./data"
import StateContext, { AppState, BodyState, GroupState, StateContextType } from "./state"
import theme from "./theme"


interface ProvidersProp {
  children: ReactNode
}

const Providers = ({children}:ProvidersProp) => {
  // Initial State
  const [menuFlg,    setMenuFlg   ] = useState<boolean>(false)
  const [appState,   setAppState  ] = useState<AppState>("TASK")
  const [groupState, setGroupState] = useState<GroupState>("SELECT")
  const [bodyState,  setBodyState ] = useState<BodyState>("IDLE")

  const StateValue:StateContextType = {
    sideMenuState: {
      state: menuFlg,
      setState: setMenuFlg
    },
    appState: {
      state: appState,
      setState: setAppState
    },
    groupState: {
      state: groupState,
      setState: setGroupState
    },
    bodyState: {
      state: bodyState,
      setState: setBodyState
    }
  }

  const DataValue:DataContextType = {
    group: {
      state: {
        id: 0,
        name: ""
      },
      setState: () => { }
    },
    groupList: {
      state: [],
      setState: () => { }
    },
    taskList: {
      state: [
        { id: 0, index: 0, name: "0000000" },
        { id: 0, index: 1, name: "1111111" },
        { id: 0, index: 2, name: "2222222" },
        { id: 0, index: 3, name: "3333333" },
        { id: 0, index: 4, name: "4444444" },
        { id: 0, index: 5, name: "5555555" },
        { id: 0, index: 6, name: "6666666" },
        { id: 0, index: 7, name: "7777777" },
      ],
      setState: () => { }
    },
    task: {
      state: {
        id: 0,
        index: 0,
        name: ""
      },
      setState: () => { }
    }
  }

  return (
      <StateContext.Provider value={StateValue}>
        <DataContext.Provider value={DataValue}>
          <ThemeProvider theme={theme}>
            <CssBaseline/>
              {children}
          </ThemeProvider>
        </DataContext.Provider>
      </StateContext.Provider>
  )
}

export default Providers