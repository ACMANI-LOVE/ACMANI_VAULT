import { ReactNode, useCallback, useState } from "react"
import ListSelector from "../molecules/listPicker"

interface ListPickerProps {
  selectList: string[]
  initialIndex: number
  noHyphen?: boolean
}
type ListPickerReturns = [
  ListPicker: ()=>ReactNode,
  selectIdx: number
]
const useListPicker = ({selectList, initialIndex, noHyphen=false}:ListPickerProps) => {
  const [selectIdx,setSelectIdx] = useState(initialIndex)
  const ListPicker = useCallback(() => {
    const handleChangeSelect = (value:string) => setSelectIdx(selectList.indexOf(value))
    return (<ListSelector list={selectList} value={selectList[selectIdx]} onChange={handleChangeSelect} noHyphen={noHyphen}/>)
  },[selectList])
  return [ListPicker, selectIdx ] as ListPickerReturns
}

export default useListPicker