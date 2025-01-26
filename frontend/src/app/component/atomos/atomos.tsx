import { Box, Button, Divider, Typography } from "@mui/material"
import { ReactNode } from "react"

interface FlexBoxProps {
  fx: number
  children: ReactNode
}
export const FlexBox = ({fx, children}:FlexBoxProps) => {
  return (<Box display={"flex"} flex={fx}>
    {children}
  </Box>)
}

interface FrameBoxProps {
  bgColor?:   string
  padding?:   string
  width?:     string
  height?:    string
  direction?: "row"|"column"
  align?:     "start"|"center"|"end"|"baseline"
  justify?:   "start"|"center"|"end"|"space-around"|"space-between"|"space-evenly"
  children: ReactNode
}
export const FrameBox = ({bgColor, direction, padding, width, height, align, justify, children}:FrameBoxProps) => {
  return (<Box display={"flex"} flexDirection={direction} width={width} height={height} alignItems={align} justifyContent={justify} padding={padding} bgcolor={bgColor}>
    {children}
  </Box>)
}

export const DividerLine = () => {
  return (<Box display={"flex"} flexDirection={"column"} paddingX={"0.5em"}>
    <Divider/>
  </Box>)
}

interface ButtonProps {
  label:   string
  textSize: "caption"
  btnType: "text"|"contained"|"outlined"
  onClick: ()=>void
}
export const ButtonComponent = ({label, textSize, btnType, onClick}:ButtonProps) => {
  return (<Button variant={btnType} onClick={onClick}>
  <Typography variant={textSize}>{label}</Typography>
</Button>)
}

interface LabelTextProps {
  text: string
}
export const LargeLabel  = ({text}:LabelTextProps) => <Typography paddingLeft={"0.5em"} variant="h6"     >{text}</Typography>
export const MediumLabel = ({text}:LabelTextProps) => <Typography paddingLeft={"0.5em"} variant="body2"  >{text}</Typography>
export const SmallLabel  = ({text}:LabelTextProps) => <Typography paddingLeft={"0.5em"} variant="caption">{text}</Typography>