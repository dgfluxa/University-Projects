# frozen_string_literal: true

class SubscribedUsersController < ApplicationController
  def update
    @study_group = StudyGroup.find(params[:study_group])
    subscribed_user = SubscribedUser.where(study_group: StudyGroup.find(params[:study_group]), user: current_user)
    if subscribed_user == []
      SubscribedUser.create(study_group: @study_group, user: current_user)
      @subscribed_user_exists = true
    else
      subscribed_user.destroy_all
      @subscribed_user_exists = false
      if @study_group.subscribed_users != []
        @study_group.update(user: @study_group.subscribed_users[0].user)
      else
        @study_group.destroy
        redirect_to(study_groups_path)
        return
      end
    end
    respond_to do |format|
      format.html {}
      format.js { render inline: 'location.reload();' }
    end
  end
end
