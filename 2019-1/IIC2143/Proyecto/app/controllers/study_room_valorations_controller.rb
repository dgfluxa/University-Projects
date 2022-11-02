# frozen_string_literal: true

class StudyRoomValorationsController < ApplicationController
  load_and_authorize_resource
  before_action :set_study_room, only: %i[new update create destroy show]
  before_action :set_user, only: %i[new update create destroy show]

  def new
    @study_room_valoration = StudyRoomValoration.new
  end

  def show
    @study_room_valoration = StudyRoomValoration.find(params[:id])
  end

  def create
    @study_room_valoration = StudyRoomValoration.new(study_room_valoration_params)
    @study_room_valoration.study_room = @study_room
    @study_room_valoration.user = @user
    if @study_room_valoration.save
      redirect_to @study_room
    else
      render 'new'
    end
  end

  def edit
    @study_room_valoration = StudyRoomValoration.find(params[:id])
  end

  def update
    @study_room_valoration = StudyRoomValoration.find(params[:id])
    if @study_room_valoration.update(study_room_valoration_params)
      redirect_to @study_room
    else
      render 'edit'
    end
  end

  def destroy
    @study_room_valoration = StudyRoomValoration.find(params[:id])
    @study_room_valoration.destroy
    redirect_to @study_room
  end

  private

  def study_room_valoration_params
    params.require(:study_room_valoration).permit(:user, :study_room, :availability, :noise, :plugs)
  end

  def set_study_room
    @study_room = StudyRoom.find(params[:study_room_id])
  end

  def set_user
    @user = current_user
  end
end
