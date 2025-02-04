import React, { Dispatch, ReactNode, SetStateAction } from "react"

export type Components = ReactNode
export type StateType<T> = {
  state:T,
  setState:Dispatch<SetStateAction<T>>
}