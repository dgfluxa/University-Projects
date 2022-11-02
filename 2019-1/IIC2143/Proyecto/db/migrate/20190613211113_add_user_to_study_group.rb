# frozen_string_literal: true

class AddUserToStudyGroup < ActiveRecord::Migration[5.1]
  def change
    add_reference :study_groups, :user, foreign_key: true
  end
end
