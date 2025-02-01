import { createTheme, CssBaseline, ThemeProvider } from "@mui/material"
import React, { createContext, Dispatch, ReactNode, SetStateAction, useState } from "react"

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
    MuiSelect: {
      styleOverrides: {
        select: {
          padding: 0,
          paddingLeft:"0.5em"
        }
      }
    },
    MuiMenuItem: {
      styleOverrides: {
        root: {
          padding: 0,
          paddingLeft:"0.5em"
        }
      }
    },
    MuiOutlinedInput: {
      styleOverrides: {
        input: {
          padding: 0,
          paddingLeft:"0.5em"
        }
      }
    },
    MuiButton: {
      styleOverrides: {
        contained: {
          padding: "0",
          alignItems:"end"
        }
      }
    }
  }
})

// Context Provider
type StateType<T> = {
  state:T,
  setState:Dispatch<SetStateAction<T>>
}
export const StateContext = createContext<{
  appState: StateType<AppState>
  groupState:StateType<GroupState>
}>({
  appState:{
    state: "-1",
    setState: ()=>{}
  },
  groupState:{
    state: "-1",
    setState: ()=>{}
  },
})

export const DataContext = createContext<{
  group: StateType<string[]>
}>({
  group: {
    state: [],
    setState: ()=>{}
  }
})

interface PropProp {
  children: ReactNode
}
const Providers = ({children}:PropProp) => {
  // Initial State
  const [appState, setAppState] = useState<AppState>("TASK")
  const [groupState, setGroupState] = useState<GroupState>("SELECT")

  const StateValue = {
    appState:{
      state: appState,
      setState: setAppState
    },
    groupState:{
      state: groupState,
      setState: setGroupState
    },
  }

  const DataValue = {
    group: {
      state: [],
      setState: ()=>{}
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

export type AppState = "-1"|"TASK"|"CONFIG"
export type GroupState = "-1"|"SELECT"|"EDIT"|"CONFIRM"

interface TaskStateProps {
  list:  string[],
  state: number
  setState: Dispatch<SetStateAction<number>>
}