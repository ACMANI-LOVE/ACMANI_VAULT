import { createTheme } from "@mui/material";

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

export default theme