# frozen_string_literal: true

class ModeratedCourse < ApplicationRecord
  belongs_to :user
  belongs_to :course
end
