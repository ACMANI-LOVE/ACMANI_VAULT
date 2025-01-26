import { ReactNode, useContext, useEffect } from "react";
import SlideAnimation from "../molucules/sideAnimation";
import { FrameBox, ButtonComponent, DividerLine, FlexBox, LargeLabel, SmallLabel, MediumLabel } from "../atomos/atomos";
import { AppState, StateContext } from "../hooks/useProviders";

interface SideMenuProps {
  open: boolean
}
const SideMenuComponent = ({open}:SideMenuProps) => {

  const { appState, taskState } = useContext(StateContext)
  const clickManageConfigs = () => appState.setState("CONFIG")
  const clickTurnBack      = () => appState.setState("TASK")

  const [RadioSelector, selectIdx] = useRadioSelector({selectList:taskState.list, initialIndex:taskState.state})
  useEffect(()=>taskState.setState(selectIdx),[selectIdx])

  const TaskSelector = () => {
    const SelectField = () => (taskState.list.length > 0)
      ? <RadioSelector/>
      : <FrameBox padding={"0.5em"} justify="center" align="center">
        <MediumLabel text={" - No Items. - "}/>
      </FrameBox>
    return (<FrameBox padding={"0.5em"} direction={"column"} width={"100%"}>
      <LargeLabel text={"Task List"}/>
      <FrameBox direction={"column"}>
        <SmallLabel text={`Now Select${taskState.state}`}/>
        <SmallLabel text={`Now Select${taskState.list[selectIdx]}`}/>
      </FrameBox>
      <DividerLine/>
      <SelectField/>
    </FrameBox>)
  }

  const ContentItem: Record<AppState, ReactNode> = {
    "-1":     <>No Items</>,
    "CONFIG": <SmallLabel text={"Config Settings."}/>,
    "TASK":   <TaskSelector/>
  }

  const ConfigButton = () => <ButtonComponent btnType={"text"} textSize={"caption"} label={"Config settings"} onClick={clickManageConfigs}/>
  const BackButton   = () => <ButtonComponent btnType={"text"} textSize={"caption"} label={"Turn Back"      } onClick={clickTurnBack     }/>

  const FooterItem: Record<AppState, ReactNode> = {
    "-1":     <>No Items</>,
    "CONFIG": <BackButton  />,
    "TASK":   <ConfigButton/>
  }

  const SideContent = () => <FrameBox direction={"row"}>{ContentItem[appState.state]}</FrameBox>
  const FooterButton = () => <FrameBox direction={"row"}>{FooterItem[appState.state]}</FrameBox>

  return (<SlideAnimation state={open} direction={"right"}>
    <FlexBox fx={1}>
      <FrameBox direction={"column"} width={"40%"} bgColor="#1111">
        <SideContent/>
        <DividerLine/>
        <FooterButton/>
      </FrameBox>
    </FlexBox>
  </SlideAnimation>);
}

export default SideMenuComponent

import { RadioGroup, FormControl } from "@mui/material";import useRadioSelector from "../hooks/useRadioSelector";

