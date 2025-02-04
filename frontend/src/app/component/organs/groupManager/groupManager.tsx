import { ReactNode, useContext } from "react"
import { FrameBox } from "../../atoms/atoms"
import StateContext, { GroupState } from "../../contexts/state"
import GroupEditor from "./groupEditor"
import GroupLabel from "./groupLabel"
import GroupSelector from "./groupSelector"

const GroupManager = () => {
  const { groupState } = useContext(StateContext)

  const PickerItem: Record<GroupState, ReactNode> = {
    "-1": <>No Items</>,
    "SELECT":  <GroupSelector/>,
    "EDIT":    <GroupEditor/>,
    "CONFIRM": <GroupLabel />
  }
  return (<FrameBox direction={"row"} width={"95%"} align={"center"} justify={"center"}>
    {PickerItem[groupState.state]}
  </FrameBox>
  )
}

export default GroupManager
