import { ReactNode, useContext, useEffect } from "react";
import SlideAnimation from "../molecules/sideAnimation";
import { FrameBox, ButtonComponent, DividerLine, FlexBox, LargeLabel, SmallLabel, MediumLabel } from "../atoms/atoms";
import { AppState, StateContext } from "../hooks/useProviders";

interface SideMenuProps {
  open: boolean
}
const SideMenuComponent = ({open}:SideMenuProps) => {

  const { appState } = useContext(StateContext)
  const clickManageConfigs = () => appState.setState("CONFIG")
  const clickTurnBack      = () => appState.setState("TASK")

  const [RadioSelector, selectIdx] = useRadioSelector({selectList:[], initialIndex:0})
  useEffect(()=>{},[selectIdx])

  const TaskSelector = () => {
    const SelectField = () => ([].length > 0)
      ? <RadioSelector/>
      : <FrameBox padding={"0.5em"} justify="center" align="center">
        <MediumLabel text={" - No Items. - "}/>
      </FrameBox>
    return (<FrameBox padding={"0.5em"} direction={"column"} width={"100%"}>
      <LargeLabel text={"Task List"}/>
      <FrameBox direction={"column"}>
        <SmallLabel text={`Now Select${0}`}/>
        <SmallLabel text={`Now Select${0}`}/>
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

