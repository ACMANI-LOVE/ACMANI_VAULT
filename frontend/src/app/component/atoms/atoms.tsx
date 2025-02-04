import MenuIcon from '@mui/icons-material/Menu'
import { Box, Button, Divider, IconButton, Typography } from "@mui/material"
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
  gap?:       string
  width?:     string
  height?:    string
  direction?: "row"|"column"
  align?:     "start"|"center"|"end"|"baseline"
  justify?:   "start"|"center"|"end"|"space-around"|"space-between"|"space-evenly"
  children: ReactNode
}
export const FrameBox = ({bgColor, direction, padding, gap, width, height, align, justify, children}:FrameBoxProps) => {
  return (<Box display={"flex"} flexDirection={direction} width={width} height={height} alignItems={align} justifyContent={justify} padding={padding} gap={gap} bgcolor={bgColor}>
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

interface IconButtonProps {
  size?: "large"|"medium"|"small"
  onClick: ()=>void
}
export const MenuIconButton = ({onClick, size="small"}:IconButtonProps) => {
  return (    <IconButton onClick={onClick}>
    <MenuIcon fontSize={size}/>
  </IconButton>)
}



interface LabelTextProps {
  text: string
}
export const LargeLabel  = ({text}:LabelTextProps) => <Typography paddingLeft={"0.5em"} variant="h6"     >{text}</Typography>
export const MediumLabel = ({text}:LabelTextProps) => <Typography paddingLeft={"0.5em"} variant="body2"  >{text}</Typography>
export const SmallLabel  = ({text}:LabelTextProps) => <Typography paddingLeft={"0.5em"} variant="caption">{text}</Typography>