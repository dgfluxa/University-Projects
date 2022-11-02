# frozen_string_literal: true

class SubscribedUser < ApplicationRecord
  belongs_to :study_group, optional: false
  belongs_to :user, optional: false
end
