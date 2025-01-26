import { Slide, Box } from "@mui/material"
import { ReactNode } from "react"

interface SlideAnimationProps {
  state:     boolean
  direction: "down"|"left"|"up"|"right"
  children:  ReactNode
}
const SlideAnimation = ({direction, state, children}:SlideAnimationProps) => {
  return (<Slide direction={direction} in={state} mountOnEnter unmountOnExit>
    <Box display={"flex"} flexDirection={"column"} flex={1}>
      {children}
    </Box>
  </Slide>)
}

export default SlideAnimation