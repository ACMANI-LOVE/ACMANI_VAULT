import { IconButton, Box, Typography } from "@mui/material";
import MenuIcon from '@mui/icons-material/Menu';
import { AppState, StateContext } from "../hooks/useProviders";
import { FrameBox, FlexBox, LargeLabel } from "../atomos/atomos";
import { ReactNode, useContext, useEffect, useState } from "react";

interface AppBarProps {
  onClick: ()=>void
}

const AppBarComponent = ({onClick}:AppBarProps) => {
  const { appState } = useContext(StateContext)

  const TitleItem: Record<AppState, ReactNode> = {
    "-1":     <>No Items</>,
    "CONFIG": <LargeLabel text={" - Config Settings. - "}/>,
    "TASK":   <>here</>
  }

  const TitleLabel = () => <FrameBox direction={"row"}>{TitleItem[appState.state]}</FrameBox>

  return (<FrameBox padding={"0.1em"} align={"center"} justify={"start"} bgColor={"#2222"}>
    <FlexBox fx={1}>
      <IconButton onClick={onClick}>
        <MenuIcon fontSize="large"/>
      </IconButton>
    </FlexBox>
    <FlexBox fx={9}>
      <TitleLabel/>
    </FlexBox>
  </FrameBox>);
}
export default AppBarComponent
