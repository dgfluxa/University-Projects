# frozen_string_literal: true

class StudyRoomComment < ApplicationRecord
  belongs_to :user
  belongs_to :study_room
end
