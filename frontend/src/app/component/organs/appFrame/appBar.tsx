import { ReactNode, useContext } from "react";
import { FlexBox, FrameBox, LargeLabel, MenuIconButton } from "../../atoms/atoms";
import StateContext, { AppState } from '../../contexts/state';
import GroupManager from '../groupManager/groupManager';

const AppBarComponent = () => {
  const { sideMenuState, appState } = useContext(StateContext)

  const TitleItem: Record<AppState, ReactNode> = {
    "-1":     <>No Items</>,
    "CONFIG": <LargeLabel text={" - Config Settings. - "}/>,
    "TASK":   <GroupManager/>
  }

  const handleClickMenu = () => sideMenuState.setState(!sideMenuState.state)
  const TitleLabel = () => <FlexBox fx={1}>{TitleItem[appState.state]}</FlexBox>

  return (<FrameBox padding={"0.1em"} align={"center"} justify={"start"} bgColor={"#2222"}>
    <MenuIconButton onClick={handleClickMenu} size={"large"}/>
    <TitleLabel/>
  </FrameBox>);
}
export default AppBarComponent
