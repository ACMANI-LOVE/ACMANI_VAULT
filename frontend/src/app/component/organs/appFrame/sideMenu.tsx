import { ReactNode, useContext } from "react";
import { ButtonComponent, DividerLine, FlexBox, FrameBox, SmallLabel } from "../../atoms/atoms";
import StateContext, { AppState } from "../../contexts/state";
import SlideAnimation from "../../molecules/sideAnimation";
import TaskSelector from "./taskSelector";

const SideMenuComponent = () => {
  const { sideMenuState, appState } = useContext(StateContext)

  const clickManageConfigs = () => appState.setState("CONFIG")
  const clickTurnBack      = () => appState.setState("TASK")

  const ConfigContents = () => {
    return (<FrameBox direction={"column"} width={"100%"}>
        <FrameBox direction={"row"} padding={"1em"}>
          <SmallLabel text={" - Config Settings. - "}/>
        </FrameBox>
        <DividerLine/>
        <FrameBox direction={"row"}>
          <ButtonComponent btnType={"text"} textSize={"caption"} label={"Turn Back"      } onClick={clickTurnBack     }/>
        </FrameBox>
    </FrameBox>);
  }

  const TaskContents = () => {
    return (<FrameBox direction={"column"} width={"100%"} >
      <FrameBox direction={"row"}>
        <TaskSelector/>
      </FrameBox>
      <DividerLine/>
      <FrameBox direction={"row"}>
        <ButtonComponent btnType={"text"} textSize={"caption"} label={"Config settings"} onClick={clickManageConfigs}/>
      </FrameBox>
    </FrameBox>);
  }

  const ContentItem: Record<AppState, ReactNode> = {
    "-1":     <>No Items</>,
    "CONFIG": <ConfigContents/>,
    "TASK":   <TaskContents/>
  }

  const SideBarContents = () => ContentItem[appState.state]

  return (<SlideAnimation state={sideMenuState.state} direction={"right"}>
    <FlexBox fx={1}>
      <FrameBox width={"100%"} bgColor="#abcf">
        <SideBarContents/>
      </FrameBox>
    </FlexBox>
  </SlideAnimation>);
}

export default SideMenuComponent
