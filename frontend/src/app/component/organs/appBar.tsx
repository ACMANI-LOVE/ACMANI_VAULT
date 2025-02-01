import { IconButton } from "@mui/material";
import MenuIcon from '@mui/icons-material/Menu';
import { AppState, StateContext } from "../hooks/useProviders";
import { FrameBox, FlexBox, LargeLabel } from "../atoms/atoms";
import { ReactNode, useContext } from "react";
import GroupSelector from "./groupManager";

interface AppBarProps {
  onClickMenu: ()=>void
}

const AppBarComponent = ({onClickMenu}:AppBarProps) => {
  const { appState } = useContext(StateContext)

  const TitleItem: Record<AppState, ReactNode> = {
    "-1":     <>No Items</>,
    "CONFIG": <LargeLabel text={" - Config Settings. - "}/>,
    "TASK":   <GroupSelector/>
  }

  const TitleLabel = () => <FlexBox fx={1}>{TitleItem[appState.state]}</FlexBox>

  return (<FrameBox padding={"0.1em"} align={"center"} justify={"start"} bgColor={"#2222"}>
    <IconButton onClick={onClickMenu}>
      <MenuIcon fontSize="large"/>
    </IconButton>
    <FlexBox fx={1}>
      <TitleLabel/>
    </FlexBox>
  </FrameBox>);
}
export default AppBarComponent
