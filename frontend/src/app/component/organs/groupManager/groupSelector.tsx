import { useContext, useEffect, useState } from "react"
import { ButtonComponent, FlexBox, FrameBox, LargeLabel } from "../../atoms/atoms"
import { DataContext } from "../../contexts/data"
import StateContext from "../../contexts/state"
import useListPicker from "../../hooks/useListPicker"

const GroupSelector = () => {
  const { groupState } = useContext(StateContext)
  const { groupList, group } = useContext(DataContext)
  const selectList = groupList.state.map((item)=>item.name)

  const [taskSelect, setTaskSelect] = useState(0)
  const [ListPiker, selectIdx] = useListPicker({selectList, initialIndex:taskSelect})
  useEffect(()=>setTaskSelect(selectIdx),[selectIdx])

  const handleClickLoad   = () => {
    group.setState(groupList.state[taskSelect])
    groupState.setState("CONFIRM")
  }
  const handleClickCreate = () => groupState.setState("EDIT")

  return (<FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"center"}>
    <FlexBox fx={8}>
      <LargeLabel text={"Period:"}/>
      <FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"space-around"}>
        <ListPiker/>
      </FrameBox>
    </FlexBox>
    <FlexBox fx={2}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
        <ButtonComponent label={"Load"} textSize={"caption"} btnType={"contained"} onClick={handleClickLoad  }/>
        <ButtonComponent label={"New"}  textSize={"caption"} btnType={"contained"} onClick={handleClickCreate}/>
      </FrameBox>
    </FlexBox>
  </FrameBox>)
}

export default GroupSelector