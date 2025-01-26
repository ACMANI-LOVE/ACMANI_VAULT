import { createTheme, CssBaseline, ThemeProvider } from "@mui/material"
import React, { Children, createContext, Dispatch, FC, ReactNode, SetStateAction, useCallback, useState } from "react"

// Theme Provider
const theme = createTheme({
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        html:    { height: "100%", width: "100%", },
        body:    { height: "100%", width: "100%", margin: 0 },
        "#root": { height: "100%", width: "100%", }
      }
    },
    MuiRadio: {
      styleOverrides: {
        root: {
          marginLeft: "0.5em",
          padding: "0.2em"
        }
      }
    },
  }
})

// Context Provider
export const StateContext = createContext<{
  appState:AppStateProps
  taskState:TaskStateProps
}>({
  appState:{
    state: "-1",
    setState: ()=>{}
  },
  taskState:{
    list: [],
    state: -1,
    setState: ()=>{}
  }
})

interface PropProp {
  children: ReactNode
}
const Providers = ({children}:PropProp) => {
  // Initial State
  const [appState, setAppState] = useState<AppState>("TASK")
  const [taskState, setTaskState] = useState<number>(0)
  const expTaskList = ["1A","2B","3C","4D"]

  return (
      <StateContext.Provider value={{
        appState:{
          state: appState,
          setState: setAppState
        },
        taskState:{
          list: expTaskList,
          // list: [],
          state: taskState,
          setState: setTaskState
        },
      }}>
        <ThemeProvider theme={theme}>
          <CssBaseline/>
            {children}
        </ThemeProvider>
      </StateContext.Provider>
  )
}

export default Providers

export type AppState = "-1"|"CONFIG"|"TASK"

interface AppStateProps {
  state: AppState
  setState: Dispatch<SetStateAction<AppState>>
}
interface TaskStateProps {
  list:  string[],
  state: number
  setState: Dispatch<SetStateAction<number>>
}