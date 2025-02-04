import { useContext, ReactNode } from "react"
import { FrameBox } from "../atoms/atoms"
import StateContext, { BodyState } from "../contexts/state"
import StandbyComponents from "../template/standby"
import RequestComponents from "../template/requests"
import PromptComponents from "../template/prompts"
import PostingComponents from "../template/postings"

const TaskPage   = () => {
  const { bodyState } = useContext(StateContext)

  const ContentItem: Record<BodyState, ReactNode> = {
    "-1": <>No Items</>,
    "IDLE"   : <StandbyComponents/>,
    "REQUEST": <RequestComponents/>,
    "PROMPT" : <PromptComponents/>,
    "POSTING": <PostingComponents/>
  }

  return (<FrameBox width="100%" align="center" justify="center" bgColor="#00F5">
    {ContentItem[bodyState.state]}
  </FrameBox>)
}

  export default TaskPage
